def palindrome_of_length_at_least_n(s):
    s = s.lower()
    n = 25
    result = set()
    for i in range(len(s)):
        for j in range(i + n, len(s) + 1):
            sub_string = s[i:j]
            if sub_string == sub_string[::-1]:
                if sub_string.isalpha():
                    result.add(sub_string)
    return result