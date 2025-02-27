def palindromes_between_indices(s):
    s = s[3:6].lower()
    chars = sorted(set(s))
    palindromes = set()

    def is_palindrome(word):
        return word == word[::-1]

    def find_palindromes(chars, word, used):
        if len(word) >= 3 and is_palindrome(word):
            palindromes.add(word)
        if len(word) < 3:
            for i, char in enumerate(chars):
                if used[i] < s.count(char):
                    find_palindromes(chars, word + char, used[:i] + [used[i] + 1] + used[i + 1:])
    find_palindromes(chars, '', [0] * len(chars))
    return palindromes