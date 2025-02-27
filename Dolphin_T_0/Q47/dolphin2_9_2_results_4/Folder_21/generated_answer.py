def palindromes_of_specific_lengths(text):
    text = text[100:296]
    result = set()
    for length in range(136, 161):
        for i in range(len(text) - length + 1):
            current_substring = text[i:i + length]
            if current_substring == current_substring[::-1] and current_substring.isalpha():
                result.add(current_substring.lower())
    return result