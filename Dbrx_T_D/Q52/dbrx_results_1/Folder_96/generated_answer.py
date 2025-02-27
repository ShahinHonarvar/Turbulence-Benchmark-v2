def palindrome_of_length_n(s: str) -> set:
    palindrome_set = set()
    if len(s) < 83:
        return palindrome_set
    for i in range(len(s) - 83 + 1):
        sub_str = s[i:i + 83].lower()
        if sub_str == sub_str[::-1]:
            palindrome_set.add(sub_str)
    return palindrome_set