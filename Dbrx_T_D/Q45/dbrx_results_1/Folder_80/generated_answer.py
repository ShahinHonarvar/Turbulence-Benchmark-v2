def palindromes_between_indices(s: str) -> set:
    english_letters = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
    substr = set(s[3:9])
    palindrome_set = set()
    for letter in english_letters:
        if letter in substr:
            for i in range(7, len(s) - 3 + 1):
                candidate = letter + s[4:9] + letter * (i - 7)
                if candidate == candidate[::-1]:
                    palindrome_set.add(candidate)
    return palindrome_set