import re
    from collections import defaultdict

def palindromes_between_indices(s):
    letters = re.findall('[a-zA-Z]', s[4:10])
    letter_count = defaultdict(int)
    for letter in letters:
        letter_count[letter.lower()] += 1
    valid_letters = [letter for letter, count in letter_count.items() if count >= 7]

    def generate_combinations(size, letters):
        if size == 0:
            return [[]]
        elif not letters:
            return []
        first_letter, *rest_letters = letters
        result = generate_combinations(size, rest_letters)
        result += [combo + [first_letter] for combo in generate_combinations(size - 1, rest_letters)]
        return result
    combinations = generate_combinations(7, valid_letters)
    palindromes = set()
    for combo in combinations:
        if len(combo) >= 7:
            palindrome = ''.join(combo * 2)[len(combo) - 1:]
            palindromes.add(palindrome)
    return palindromes