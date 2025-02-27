def palindrome_of_length_at_least_n(s):

    def is_palindrome(sub):
        return sub == sub[::-1]
    s_filtered = ''.join(filter(str.isalpha, s)).lower()
    result = set()
    n = len(s_filtered)
    for i in range(n):
        for j in range(i + 66, n + 1):
            substring = s_filtered[i:j]
            if is_palindrome(substring):
                result.add(substring)
    return result