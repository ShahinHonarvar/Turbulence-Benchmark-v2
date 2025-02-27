def return_n_smallest_chars(text):
    new_text = sorted(text)
    final_text = new_text[:46]
    final_text.sort(reverse=True)
    return final_text