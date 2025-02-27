def palindromes_of_specific_lengths(given_str):
    """Returns a set of all palindromes meeting the given requirements."""
    palindrome_set = set()
    'Convert the string to lowercase for case-insensitive validation'
    lowered_str = given_str.lower()
    'Find palindromes of lengths 3 to 15 within the substring [0:100]'
    for i in range(0, 101):
        for j in range(3, 16):
            'Check if the substring is a palindrome'
            if lowered_str[i:i + j] == lowered_str[i:i + j][::-1]:
                palindrome_set.add(given_str[i:i + j])
    return palindrome_set