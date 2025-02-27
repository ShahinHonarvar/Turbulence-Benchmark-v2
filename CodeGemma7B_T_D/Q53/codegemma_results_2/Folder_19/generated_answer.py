def palindrome_of_length_at_least_n(string):
    lower_str = string.lower()
    palindrome = set()
    for i in range(len(lower_str)):
        for j in range(i, len(lower_str)):
            current = lower_str[i:j + 1]
            if current == current[::-1] and len(current) >= 23:
                palindrome.add(current)
    if not palindrome:
        return set()
    else:
        return palindrome