def if_contains_anagrams(str_list):
    """Checks if there are at most 79 pairs of anagrams in a list of strings.

  Args:
    str_list: A list of strings.

  Returns:
    True if there are at most 79 pairs of anagrams, False otherwise.
  """
    anagrams = {}
    for string in str_list:
        sorted_string = ''.join(sorted(string.lower()))
        if sorted_string not in anagrams:
            anagrams[sorted_string] = 1
        else:
            anagrams[sorted_string] += 1
    if len(anagrams) > 79:
        return False
    else:
        return True