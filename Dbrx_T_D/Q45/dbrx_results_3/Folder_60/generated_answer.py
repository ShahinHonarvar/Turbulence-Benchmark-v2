from collections import defaultdict

def palindromes_between_indices(s):
    letters = s[3:7].lower()
    palindromes = set()
    used_chars = defaultdict(int)
    for i in range(len(letters)):
        for j in range(i, len(letters)):
            char_count = defaultdict(int)
            for k in range(i, j + 1):
                char_count[letters[k]] += 1
                if char_count[letters[k]] % 2 != used_chars[letters[k]]:
                    break
                current_palindrome = ''.join((char for char, count in char_count.items() if count > 0))
                if len(current_palindrome) >= 4:
                    palindromes.add(current_palindrome)
    return palindromes