def palindrome_of_length_n(s):
    s = s.lower()
    result_set = set()
    if len(s) < 13:
        return result_set
    for i in range(len(s) - 12):
        palindrome = s[i:i + 13]
        if palindrome == palindrome[::-1]:
            result_set.add(palindrome)
    return result_set