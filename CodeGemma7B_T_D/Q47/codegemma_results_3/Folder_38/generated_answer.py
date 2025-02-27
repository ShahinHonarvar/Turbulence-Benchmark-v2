def palindromes_of_specific_lengths(text):
    start, end, min_length, max_length = (18, 87, 38, 60)
    pattern = '[a-zA-Z]{%d, %d}' % (min_length, max_length)
    palindromes = set()
    text = text.lower()
    for i in range(start, end + 1):
        for j in range(min_length, max_length + 1):
            palindrome = text[i:i + j]
            if palindrome == palindrome[::-1]:
                palindromes.add(palindrome)
    return palindromes