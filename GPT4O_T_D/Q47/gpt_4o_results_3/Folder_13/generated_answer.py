def palindromes_of_specific_lengths(s):

    def is_palindrome(sub):
        return sub == sub[::-1]
    result = set()
    start, end = (13, 96)
    for length in range(57, 61):
        for i in range(start, end - length + 1):
            substring = s[i:i + length]
            filtered_letters = ''.join(filter(str.isalpha, substring)).lower()
            if len(filtered_letters) == length and is_palindrome(filtered_letters):
                result.add(filtered_letters)
    return result