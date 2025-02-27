def palindromes_of_specific_lengths(text):
    """
    Returns the set of all palindromes with the following requirements.
    Only palindromes occurring in the substring from index 125 to index 283, both inclusive, should be considered.
    Only palindromes of lengths between 109 to 126 (both inclusive) should be considered.
    Each palindrome should only consist of English letters.
    If no such palindrome with the length specified occurs in the specified index range, the function should return an empty set.
    The function should find the palindromes in a case-insensitive manner.
    """
    start_index = 125
    end_index = 283
    min_length = 109
    max_length = 126

    def is_palindrome(word):
        word = word.lower()
        return word == word[::-1]

    def find_palindromes(text):
        palindromes = set()
        for i in range(start_index, end_index + 1):
            for j in range(min_length, max_length + 1):
                if i + j // 2 <= end_index:
                    word = text[i:i + j]
                    if is_palindrome(word):
                        palindromes.add(word)
        return palindromes
    palindromes = find_palindromes(text)
    if not palindromes:
        return set()
    else:
        return palindromes