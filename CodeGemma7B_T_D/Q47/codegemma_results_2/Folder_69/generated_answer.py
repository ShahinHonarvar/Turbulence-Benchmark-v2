def palindromes_of_specific_lengths(word):
    result = set()
    word = word.lower()
    for start in range(11, 97):
        for end in range(start + 44, 97):
            current_palindrome = word[start:end + 1]
            if current_palindrome == current_palindrome[::-1]:
                result.add(current_palindrome)
    return result if result else set()