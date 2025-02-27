def all_substring_of_size_n(s):
    """
    Search all substring with lenght n in given string without duplicate characters
  """
    results = set()
    for i in range(len(s)):
        for j in range(i + 40, len(s)):
            if len(set(s[i:j])) == 40:
                results.add(s[i:j])
    return list(results)