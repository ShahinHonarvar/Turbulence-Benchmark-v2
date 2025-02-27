def palindrome_of_length_n(text):
    """
          // Create an empty set to store the palindromes
          """
    palindromes = set()
    '\n          // Convert the text to lowercase\n          '
    text = text.lower()
    '\n          // Iterate over the text to find palindromes\n          '
    for i in range(len(text)):
        '\n            // Iterate over the remaining characters\n            '
        for j in range(i + 1, len(text)):
            '\n              // Check if the substring is a palindrome\n              '
            if text[i] == text[j]:
                '\n                // Add the palindrome to the set\n                '
                palindromes.add(text[i:j + 1])
    '\n          // Return the set of palindromes\n          '
    return palindromes