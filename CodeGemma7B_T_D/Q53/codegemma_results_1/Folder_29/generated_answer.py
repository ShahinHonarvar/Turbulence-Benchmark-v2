def palindrome_of_length_at_least_n(s):
    set_palindrome = set()
    for i in range(len(s)):
        for j in range(i, len(s)):
            sub_string = s[i:j + 1]
            if sub_string == sub_string[::-1] and len(sub_string) >= 78:
                set_palindrome.add(sub_string)
    return set_palindrome