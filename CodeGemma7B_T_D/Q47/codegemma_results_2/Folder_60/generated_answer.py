def palindromes_of_specific_lengths(text):
    """
        :type text: str
        :rtype: dict[int, list[str]]
        """
    if not text:
        return {}
    text_lower = text[23:82].lower()
    palindromes = {}
    for i in range(len(text_lower) - 32):
        for j in range(i + 32, len(text_lower)):
            if text_lower[i:j + 1] == text_lower[j:i:-1]:
                length = j - i + 1
                if length not in palindromes:
                    palindromes[length] = []
                palindromes[length].append(text_lower[i:j + 1])
    return palindromes