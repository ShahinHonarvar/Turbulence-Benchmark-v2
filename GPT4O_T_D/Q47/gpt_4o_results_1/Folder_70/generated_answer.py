def palindromes_of_specific_lengths(s):

    def is_palindrome(sub):
        return sub.lower() == sub.lower()[::-1]
    english_letters = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
    filtered_substring = ''.join((char for char in s[10:71] if char in english_letters))
    result = set()
    for length in range(24, 53):
        for i in range(len(filtered_substring) - length + 1):
            candidate = filtered_substring[i:i + length]
            if is_palindrome(candidate):
                result.add(candidate)
    return result