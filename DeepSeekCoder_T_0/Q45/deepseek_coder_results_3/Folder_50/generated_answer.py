def palindromes_between_indices(s):

    def is_palindrome(word):
        return word == word[::-1]
    letters = set(s[4:9].lower())
    palindromes = set()
    for i in range(2 ** len(letters)):
        combination = ''.join(sorted([letters.pop() for _ in range(5) if i & 1 << _]))
        if len(combination) == 5 and is_palindrome(combination):
            palindromes.add(combination)
    return palindromes