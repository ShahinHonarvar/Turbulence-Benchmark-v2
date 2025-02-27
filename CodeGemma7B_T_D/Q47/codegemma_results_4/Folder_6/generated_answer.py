def palindromes_of_specific_lengths(text):
    text = text.lower()
    palindrome_set = set()
    for i in range(45, 99):
        for j in range(40, 48):
            current_palindrome = text[i - j:i + 1]
            if current_palindrome == current_palindrome[::-1]:
                palindrome_set.add(current_palindrome)
    return palindrome_set