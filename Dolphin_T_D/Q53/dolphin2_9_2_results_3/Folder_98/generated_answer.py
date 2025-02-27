def palindrome_of_length_at_least_n(s):
    s = s.lower()
    n = 6
    result_set = set()
    for length in range(n, len(s) + 1):
        for i in range(len(s) - length + 1):
            if s[i:i + length] == s[i:i + length][::-1] and s[i:i + length].isalpha():
                result_set.add(s[i:i + length])
    return result_set