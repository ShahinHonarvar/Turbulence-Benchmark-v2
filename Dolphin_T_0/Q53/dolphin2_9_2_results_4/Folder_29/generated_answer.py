def palindrome_of_length_at_least_n(s):
    s = s.lower()
    set_result = set()
    for i in range(len(s) - 77):
        for j in range(78, len(s) - i + 1):
            if s[i:i + j] == s[i:i + j][::-1]:
                set_result.add(s[i:i + j])
    return set_result