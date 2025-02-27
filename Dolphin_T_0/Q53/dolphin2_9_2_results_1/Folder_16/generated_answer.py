def palindrome_of_length_at_least_n(text):
    result = set()
    text = text.lower()
    for length in range(119, len(text) + 1):
        for start in range(len(text) - length + 1):
            end = start + length - 1
            if text[start:end + 1] == text[start:end + 1][::-1] and text[start:end + 1].isalpha():
                result.add(text[start:end + 1])
    return result