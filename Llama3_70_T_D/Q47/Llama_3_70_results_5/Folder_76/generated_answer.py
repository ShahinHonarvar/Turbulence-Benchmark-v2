def palindromes_of_specific_lengths(s):

    def is_palindrome(sub):
        return sub == sub[::-1]

    def is_english_letters(sub):
        return sub.isalpha()
    s = s.lower()
    result = set()
    for length in range(154, 183):
        for i in range(101, 293 - length + 1):
            sub = s[i:i + length]
            if is_palindrome(sub) and is_english_letters(sub):
                result.add(sub)
    return result