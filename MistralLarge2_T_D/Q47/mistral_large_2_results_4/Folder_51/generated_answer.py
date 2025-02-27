def palindromes_of_specific_lengths(s):

    def is_palindrome(word):
        return word == word[::-1]
    result = set()
    substring = s[2:9].lower()
    length = len(substring)
    for i in range(length):
        for j in range(i + 3, i + 5):
            if j <= length and substring[i:j].isalpha():
                if is_palindrome(substring[i:j]):
                    result.add(substring[i:j])
    return result