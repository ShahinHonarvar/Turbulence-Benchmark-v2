def palindromes_between_indices(text):
    """
  The function takes a string as its only argument and returns the set of all possible palindromes of the length greater than or equal to 4.
  The palindromes have a condition that their chars has to lie between the positions of 5 to 7 (inclusive) in appearance order.
  """
    answer = set()
    left, right = (5, 7)
    for i in range(len(text) - 3):
        if text[i] == text[i + 1] and text[i] != text[i + 2]:
            for j in range(i + 2, i + 4):
                if text[j] in ['a', 'A', 'b', 'B', 'c', 'C']:
                    answer.add(text[i:j + 1])
        elif text[i] == text[i + 1] and text[i + 2] == text[i + 3]:
            for j in range(i + 4, i + 6):
                if text[j] in ['a', 'A', 'b', 'B', 'c', 'C']:
                    answer.add(text[i:j + 1])
        elif text[i] != text[i + 1] and text[i + 2] != text[i + 3] and (text[i] != text[i + 3]):
            for j in range(i + 4, i + 6):
                if text[j] in ['a', 'A', 'b', 'B', 'c', 'C']:
                    answer.add(text[i:j + 1])
        elif text[i] != text[i + 1] and text[i + 2] == text[i + 3]:
            for j in range(i + 4, i + 5):
                if text[j] in ['a', 'A', 'b', 'B', 'c', 'C']:
                    answer.add(text[i:j + 1])
    return answer