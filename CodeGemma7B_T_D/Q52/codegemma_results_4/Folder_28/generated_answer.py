def palindrome_of_length_n(text):
    """
            This function takes a string as an argument and returns the set of all palindromes of the length equal to 43.
            """
    lower_text = text.lower()
    size = len(lower_text)
    answer_set = set()
    for i in range(size):
        for j in range(i, size):
            substring = lower_text[i:j + 1]
            if substring == substring[::-1]:
                answer_set.add(substring)
    return answer_set