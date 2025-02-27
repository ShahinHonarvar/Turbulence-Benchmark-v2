def return_n_smallest_chars(str):
    """
  """

    def fix_it(x):
        return ord(x)
    data = sorted(str, key=fix_it, reverse=True)[0:9]
    return data