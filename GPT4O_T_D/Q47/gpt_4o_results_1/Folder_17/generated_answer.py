def palindromes_of_specific_lengths(s):

    def is_palindrome(sub):
        return sub.lower() == sub[::-1].lower()

    def filter_letters(sub):
        return ''.join(filter(str.isalpha, sub))
    s = filter_letters(s[22:96])
    result = set()
    for length in range(52, 56):
        for i in range(len(s) - length + 1):
            substring = s[i:i + length]
            if is_palindrome(substring):
                result.add(substring)
    return result