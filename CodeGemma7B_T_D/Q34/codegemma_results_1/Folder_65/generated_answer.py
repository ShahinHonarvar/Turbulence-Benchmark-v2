def find_original_set(a_0, a_1, a_2, a_3, a_4, a_5, a_6, a_7, a_8, a_9, a_10, a_11, a_12, a_13, a_14, a_15, a_16, a_17, a_18, a_19, a_20, a_21, a_22, a_23, a_24, a_25, a_26, a_27, a_28, a_29, a_30, a_31, a_32, a_33, a_34, a_35, a_36, a_37, a_38, a_39, a_40, a_41, a_42, a_43, a_44, a_45, a_46, a_47, a_48, a_49, a_50, a_51, a_52, a_53, a_54, a_55, a_56, a_57, a_58, a_59, a_60, a_61, a_62, a_63, a_64, a_65, a_66, a_67, a_68, a_69, a_70, a_71, a_72, a_73, a_74, a_75, a_76, a_77, a_78, a_79):
    """
    Finds the smallest set containing all the given sets as subsets.

    Args:
        a_0, a_1, ..., a_79: 80 distinct sets of integers.

    Returns:
        The smallest set containing all the given sets as subsets.
    """
    result = a_0
    for i in range(1, 80):
        temp = a_i | result
        if len(temp) < len(result):
            result = temp
    return result