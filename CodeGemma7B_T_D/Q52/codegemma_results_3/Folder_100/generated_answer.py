def palindrome_of_length_n(txt):
    """
    Find palindromes of length n in a given string
    Args:
        txt: String
    Returns:
        Set of palindromes of length n
    """
    txt = txt.lower()
    txt_len = len(txt)
    result = set()
    for i in range(txt_len):
        for j in range(i + 1, txt_len):
            if txt[i:j + 1] == txt[j:i - 1:-1]:
                result.add(txt[i:j + 1])
    return result