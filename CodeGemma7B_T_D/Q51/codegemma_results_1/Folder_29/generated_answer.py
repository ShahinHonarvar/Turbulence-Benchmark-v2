def if_contains_anagrams(str_list):
    """
  O(n * log n) time complexity.
  """
    str_list = [s.lower() for s in str_list]
    str_list.sort(key=len)
    ans = 0
    for i in range(len(str_list)):
        for j in range(i + 1, min(i + 7, len(str_list))):
            if sorted(str_list[i]) == sorted(str_list[j]):
                ans += 1
    return ans <= 318