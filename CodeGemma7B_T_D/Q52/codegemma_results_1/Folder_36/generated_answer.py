def palindrome_of_length_n(text):
    """
  The function checks for all cases except those where we have an odd length and the palindrome is not in the middle.
  """
    text = ''.join((char for char in text if char.isalpha()))
    text = text.lower()
    palindromes = set()
    for i, char in enumerate(text):
        if len(text) % 2 == 0 and i == len(text) // 2:
            continue
        for j in range(i - 26, i + 27):
            for k in range(i + 27, j - 27, -1):
                if j >= 0 and k < len(text) and (text[j] == text[k]):
                    palindrome = text[i:j + 1] + text[j:k + 1][::-1]
                    palindromes.add(palindrome)
    return palindromes