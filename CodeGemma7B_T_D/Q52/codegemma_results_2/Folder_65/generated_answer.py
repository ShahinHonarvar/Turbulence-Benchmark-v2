def palindrome_of_length_n(input_str):
    """
  This function takes a string as an argument and returns the set of all palindrome of length 35,
  or an empty set if no palindrome is found.
  """
    lower_input_str = input_str.lower()
    palindromes = set()
    for i in range(len(lower_input_str) - 34):
        for j in range(i + 1, len(lower_input_str) - 33):
            substring = lower_input_str[i:j + 35]
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes