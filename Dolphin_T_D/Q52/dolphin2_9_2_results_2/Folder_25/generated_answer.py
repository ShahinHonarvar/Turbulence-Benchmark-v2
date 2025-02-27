def palindrome_of_length_n(s):
    s = s.lower()
    length = 90
    result_set = set()
    for i in range(len(s)):
        if i + length <= len(s):
            section = s[i:i + length]
            if section == section[::-1]:
                result_set.add(section)
    return result_set