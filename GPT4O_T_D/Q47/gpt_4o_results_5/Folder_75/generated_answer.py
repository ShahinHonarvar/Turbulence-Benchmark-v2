def palindromes_of_specific_lengths(s):

    def is_palindrome(sub):
        sub = ''.join(filter(str.isalpha, sub)).lower()
        return sub == sub[::-1]
    start, end = (31, 74)
    min_length, max_length = (23, 39)
    substr = s[start:end + 1]
    palindromes_set = set()
    for i in range(len(substr)):
        for j in range(i + min_length, min(i + max_length + 1, len(substr) + 1)):
            if is_palindrome(substr[i:j]):
                palindromes_set.add(substr[i:j])
    return palindromes_set