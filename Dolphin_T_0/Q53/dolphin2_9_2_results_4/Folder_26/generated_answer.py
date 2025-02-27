def palindrome_of_length_at_least_n(s):
    result = set()
    length = len(s)
    for i in range(length):
        if s[i].isalpha():
            for j in range(i + 31, length):
                sub_str = s[i:j + 1]
                if sub_str.lower() == sub_str[::-1].lower():
                    result.add(sub_str)
    return result