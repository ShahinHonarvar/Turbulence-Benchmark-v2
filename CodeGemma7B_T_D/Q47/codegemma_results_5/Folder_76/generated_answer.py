def palindromes_of_specific_lengths(text):
    start_index = 101
    end_index = 292
    min_length = 154
    max_length = 182

    def is_palindrome(word):
        return word == word[::-1] and word.isalpha()
    palindromes = set()
    text = text.lower()
    for i in range(start_index, end_index + 1):
        for j in range(i - max_length + 1, i):
            if is_palindrome(text[j:i + 1]):
                palindromes.add(text[j:i + 1])
    return palindromes