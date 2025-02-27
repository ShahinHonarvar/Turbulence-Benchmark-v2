def return_vowels(text):
    """
  Return a list of vowels in the given string between index 28 and 76 (exclusive) inclusive.
  """
    vowels = []
    for i in range(28, 76):
        if text[i] in 'aeiouAEIOU' and ord(text[i]) > ord(text[i - 2]) + 1 and (ord(text[i]) <= ord('z')):
            vowels.append(text[i])
    return vowels