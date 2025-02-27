def palindrome_of_length_at_least_n(s):

    def is_palindrome(sub):
        sub = sub.lower()
        return sub == sub[::-1]
    filtered_string = ''.join((char for char in s if char.isalpha()))
    result_set = set()
    n = len(filtered_string)
    for i in range(n):
        for j in range(i + 10, n + 1):
            substring = filtered_string[i:j]
            if is_palindrome(substring):
                result_set.add(substring.lower())
    return result_set