def palindrome_of_length_at_least_n(text):
    """
    This function returns the set of all palindromes of the length greater than or equal to 81.
    """
    text = text.lower()
    output = set()
    for i in range(len(text)):
        for j in range(i + 1, len(text)):
            for k in range(j + 1, len(text)):
                for l in range(k + 1, len(text)):
                    for m in range(l + 1, len(text)):
                        for n in range(m + 1, len(text)):
                            word = text[i:j + 1] + text[j + 1:k + 1][::-1]
                            if len(word) >= 81 and word.isalpha():
                                output.add(word)
    return output