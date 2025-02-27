def palindromes_between_indices(s: str) -> set:

    def is_palindrome(word):
        return word == word[::-1]
    palindromes = set()
    english_letters = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
    for i in range(1, 6):
        for j in range(i + 1, 6):
            substring = s[i:j]
            if substring.isalpha() and substring.lower() in english_letters:
                for k in range(i, j):
                    for l in range(k + 1, j):
                        sub_sub_string = s[k:l]
                        if sub_sub_string.isalpha() and sub_sub_string.lower() in english_letters:
                            palindrome = substring + sub_sub_string + substring
                            if is_palindrome(palindrome) and len(palindrome) >= 6:
                                palindromes.add(palindrome)
    return palindromes