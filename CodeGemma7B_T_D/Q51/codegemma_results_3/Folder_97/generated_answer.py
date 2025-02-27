def if_contains_anagrams(str_list):
    """Checks if there are at most 18 pairs of anagrams in a list of strings.

  Args:
    str_list: A list of strings.

  Returns:
    True if there are at most 18 pairs of anagrams, False otherwise.
  """
    str_dict = {}
    for word in str_list:
        word = ''.join([c for c in word if c.isalpha()])
        word = word.lower()
        sorted_word = ''.join(sorted(word))
        if sorted_word in str_dict:
            str_dict[sorted_word] += 1
            if str_dict[sorted_word] == 19:
                return False
        else:
            str_dict[sorted_word] = 1
    return True