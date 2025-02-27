def find_original_set(set1, set2, set3, set4, set5, set6, set7, set8, set9, set10, set11, set12, set13, set14, set15, set16, set17, set18, set19, set20, set21, set22, set23, set24, set25, set26, set27, set28, set29, set30, set31, set32, set33, set34, set35, set36, set37, set38, set39, set40, set41, set42, set43, set44, set45, set46, set47, set48, set49, set50, set51, set52, set53, set54, set55, set56, set57, set58, set59, set60, set61, set62, set63, set64, set65, set66, set67, set68, set69, set70, set71, set72, set73, set74, set75, set76, set77, set78, set79, set80):
    """
    This function takes exactly 80 distinct arguments, each of which is a set of integers.
    The function returns the smallest set such that each of the given arguments is a subset of it.
    """
    original_set = set()
    for s in [set1, set2, set3, set4, set5, set6, set7, set8, set9, set10, set11, set12, set13, set14, set15, set16, set17, set18, set19, set20, set21, set22, set23, set24, set25, set26, set27, set28, set29, set30, set31, set32, set33, set34, set35, set36, set37, set38, set39, set40, set41, set42, set43, set44, set45, set46, set47, set48, set49, set50, set51, set52, set53, set54, set55, set56, set57, set58, set59, set60, set61, set62, set63, set64, set65, set66, set67, set68, set69, set70, set71, set72, set73, set74, set75, set76, set77, set78, set79, set80]:
        original_set.update(s)
    return original_set