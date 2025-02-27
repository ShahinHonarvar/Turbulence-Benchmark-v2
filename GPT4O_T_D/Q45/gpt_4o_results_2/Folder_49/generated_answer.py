from collections import Counter

def palindromes_between_indices(s):
    if len(s) < 8:
        return set()
    sub_str = s[5:8].lower()
    letters = [c for c in sub_str if c.isalpha()]
    palindromes = set()

    def is_palindrome(s):
        return s == s[::-1]

    def backtrack(path, counter):
        if len(path) >= 3 and is_palindrome(path):
            palindromes.add(path)
        for letter in counter:
            if counter[letter] > 0:
                counter[letter] -= 1
                backtrack(path + letter, counter)
                counter[letter] += 1
    letter_count = Counter(letters)
    backtrack('', letter_count)
    return palindromes