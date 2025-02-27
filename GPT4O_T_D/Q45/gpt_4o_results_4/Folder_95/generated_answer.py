from collections import Counter
            from itertools import permutations

def palindromes_between_indices(s):

    def can_form_palindrome(letters):
        counter = Counter(letters)
        odd_count = 0
        for val in counter.values():
            if val % 2 != 0:
                odd_count += 1
            if odd_count > 1:
                return False
        return True
    result_set = set()
    if len(s) < 9:
        return result_set
    letters = ''.join(filter(str.isalpha, s[7:9])).lower()
    if can_form_palindrome(letters):

        def generate_palindromes(half):
            seen = set()
            for p in permutations(half):
                p_str = ''.join(p)
                if p_str not in seen:
                    seen.add(p_str)
                    result_set.add(p_str + p_str[::-1])
                    for mid in set(letters):
                        if letters.count(mid) % 2 != 0:
                            result_set.add(p_str + mid + p_str[::-1])
        half = []
        char_count = {}
        for char in letters:
            char_count[char] = char_count.get(char, 0) + 1
        for char, count in char_count.items():
            half.extend([char] * (count // 2))
        generate_palindromes(half)
    return {p for p in result_set if len(p) >= 3}