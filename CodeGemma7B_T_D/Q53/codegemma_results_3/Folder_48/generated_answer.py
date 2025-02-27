def palindrome_of_length_at_least_n(text):
    result = set()
    pattern = '[A-Za-z]{150,}'
    for match in re.finditer(pattern, text):
        palindrome = match.group()
        if palindrome == palindrome[::-1]:
            result.add(palindrome)
    return result