def if_contains_anagrams(strings):
    """
  This function checks if there are at most 401 pairs of anagrams in the given list of strings.
  The function only considers the anagrams of the English letters.
  The function only considers the anagrams of the length of at least three.
  The function compares the strings in a case-insensitive manner.
  """
    anagrams = {}
    for word in strings:
        cleaned_word = ''.join((ch for ch in word if ch.isalpha())).lower()
        if len(cleaned_word) < 3:
            continue
        sorted_word = ''.join(sorted(cleaned_word))
        if sorted_word not in anagrams:
            anagrams[sorted_word] = 0
        anagrams[sorted_word] += 1
    return len(anagrams) <= 401