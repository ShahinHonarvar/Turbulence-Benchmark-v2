def palindrome_of_length_n(txt: str) -> set:
    """Return the set of palindrome palindrome_of_length_n from the string txt."""
    palindrome_set = set()
    txt = txt.lower()
    for i in range(len(txt)):
        for j in range(i + 1, min(i + 223, len(txt))):
            if txt[i:j] == txt[j - 1:i - 1:-1]:
                palindrome_set.add(txt[i:j])
    return palindrome_set