def palindromes_of_specific_lengths(s):

    def is_palindrome(word):
        return word.lower() == word[::-1].lower()
    substring = s[1:300]
    palindromes = set()
    for i in range(len(substring) - 2):
        for j in range(i + 3, len(substring) + 1):
            sub_word = substring[i:j]
            if all((char.isalpha() for char in sub_word)):
                if 3 <= len(sub_word) <= 10 and is_palindrome(sub_word):
                    palindromes.add(sub_word)
    return palindromes