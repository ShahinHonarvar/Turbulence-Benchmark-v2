def return_vowels(string):
    """
  Returns a list of all vowel English letters between index 55 (inclusive) and index 65 (exclusive)
  that are greater than character Z and smaller than or equal to character w.
  
  If no such characters exist in the specified range, the function should return an empty list.
  """
    vowels = []
    for char in string[55:65]:
        if char in 'aeiouAEIOU' and char > 'Z' and (char <= 'w'):
            vowels.append(char)
    return vowels